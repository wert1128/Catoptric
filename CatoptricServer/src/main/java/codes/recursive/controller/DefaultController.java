package codes.recursive.controller;

import codes.recursive.Command;
import io.micronaut.core.util.CollectionUtils;
import io.micronaut.http.HttpResponse;
import io.micronaut.http.MediaType;
import io.micronaut.http.annotation.*;

import java.io.*;
import java.util.Map;

@Controller("/")
public class DefaultController {
    public String run_command(String args) throws IOException{
        //Process p = Runtime.getRuntime().exec("python ./CatoptricController.py.py" + args);
        Process p = Runtime.getRuntime().exec("python ../CatoptricController.py " + args);
        BufferedReader in = new BufferedReader(new InputStreamReader(p.getInputStream()));
        String ret = in.readLine();
        return ret;
    }

    @Get(value="test", produces = MediaType.APPLICATION_JSON)
    public HttpResponse<Map<String, Object>> test() throws IOException{
        String ret = run_command("test");
        return HttpResponse.ok(
            CollectionUtils.mapOf(
                    "status", ret
            )
        );
    }

    @Get(value="quit", produces = MediaType.APPLICATION_JSON)
    public HttpResponse<Map<String, Object>> quit() throws IOException{
        String ret = run_command("quit");
        return HttpResponse.ok(
                CollectionUtils.mapOf(
                        "status", ret
                )
        );
    }

    @Post(value = "move", consumes = MediaType.APPLICATION_JSON, produces = MediaType.APPLICATION_JSON)
    public HttpResponse<Map<String, Object>> move(Command command) throws IOException{

        String motor = command.getMotor();
        String direction = command.getDirection();
        String steps = command.getSteps();
        String args = "move "+motor+" "+direction+" "+steps;
        String ret = run_command(args);
        return HttpResponse.ok(
                CollectionUtils.mapOf(
                        "motor", motor,
                        "direction", direction,
                        "steps", steps,
                        "status", ret
                        )
        );
    }
}