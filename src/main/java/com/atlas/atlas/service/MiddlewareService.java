package com.atlas.atlas.service;

import org.json.JSONArray;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class MiddlewareService {

    public String executePythonScript(String scriptName, String... args) {
        String jsonResponse = "";
        try {
            ProcessBuilder pb = new ProcessBuilder(buildCommand(scriptName, args));
            Process process = pb.start();
            process.waitFor();

            jsonResponse = readOutput(process);
            System.out.println("JSON Response: " + jsonResponse);
            readErrors(process);

            process.waitFor();
        } catch (IOException | InterruptedException e) {
            e.printStackTrace();
        }
        return jsonResponse;
    }

    private String[] buildCommand(String scriptName, String[] args) {
        String[] baseCommand = {"venv/bin/python3.9", "src/main/resources/com/atlas/atlas/scripts/" + scriptName + ".py"};
        String[] command = new String[baseCommand.length + args.length];
        System.arraycopy(baseCommand, 0, command, 0, baseCommand.length);
        System.arraycopy(args, 0, command, baseCommand.length, args.length);
        return command;
    }

    private String readOutput(Process process) {
        try {
            BufferedReader reader = new BufferedReader(new InputStreamReader(process.getInputStream()));
            StringBuilder output = new StringBuilder();
            String line;
            while ((line = reader.readLine()) != null) {
                output.append(line);
            }
            return output.toString();
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }

    private void readErrors(Process process) {
        try {
            BufferedReader reader = new BufferedReader(new InputStreamReader(process.getErrorStream()));
            StringBuilder output = new StringBuilder();
            String line;
            while ((line = reader.readLine()) != null) {
                output.append(line);
                System.out.println("Error: " + line);
            }
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }

    public JSONArray parseResponse(String jsonResponse) {
        return new JSONArray(jsonResponse);
    }
}
