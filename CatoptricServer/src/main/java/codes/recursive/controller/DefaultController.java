package codes.recursive.controller;

import codes.recursive.Command;
import io.micronaut.core.util.CollectionUtils;
import io.micronaut.http.HttpResponse;
import io.micronaut.http.MediaType;
import io.micronaut.http.annotation.*;
import java.util.Map;
@Controller("/")
public class DefaultController {

    @Get(value="test", produces = MediaType.APPLICATION_JSON)
    public HttpResponse<Map<String, Object>> test() {
        return HttpResponse.ok(
            CollectionUtils.mapOf(
                    "status", "success"
            )
        );
    }

    @Get(value="quit", produces = MediaType.APPLICATION_JSON)
    public HttpResponse<Map<String, Object>> quit() {
        return HttpResponse.ok(
                CollectionUtils.mapOf(
                        "status", "quit success"
                )
        );
    }

    @Post(value = "run", consumes = MediaType.APPLICATION_JSON, produces = MediaType.APPLICATION_JSON)
    public HttpResponse<Map<String, Object>> run(Command command) {

        Integer motor = command.getMotor();
        Boolean direction = command.getDirection();
        Integer steps = command.getSteps();
        return HttpResponse.ok(
                CollectionUtils.mapOf(
                        "motor", motor,
                        "direction", direction,
                        "steps", steps
                        )
        );
    }

}