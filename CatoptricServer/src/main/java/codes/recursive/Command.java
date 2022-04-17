package codes.recursive;
import io.micronaut.core.annotation.Introspected;

@Introspected
public class Command {
    private Integer motor;
    private Boolean direction;
    private Integer steps;

    public Integer getMotor() {
        return motor;
    }
    public void setMotor(Integer motor) {
        this.motor = motor;
    }

    public Integer getSteps() {
        return steps;
    }
    public void setSteps(Integer steps) {
        this.steps = steps;
    }

    public Boolean getDirection() {
        return direction;
    }
    public void setDirection(Boolean direction) {
        this.direction = direction;
    }

}
