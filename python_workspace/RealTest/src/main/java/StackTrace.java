import java.util.List;

public class StackTrace {
    private final String exception;
    private final String reason;
    private final List<String> foundFrames;
    private boolean cause;
    private int traceStart;
    private int traceEnd;

    public StackTrace(String exception, String reason, List<String> foundFrames) {
        this.exception = exception;
        this.reason = reason;
        this.foundFrames = foundFrames;
    }

    public void setCause(boolean cause) {
        this.cause = cause;
    }

    public void setTraceStart(int traceStart) {
        this.traceStart = traceStart;
    }

    public void setTraceEnd(int traceEnd) {
        this.traceEnd = traceEnd;
    }

    public String getException() {
        return exception;
    }

    public String getReason() {
        return reason;
    }

    public List<String> getFoundFrames() {
        return foundFrames;
    }

    public boolean isCause() {
        return cause;
    }

    public int getTraceStart() {
        return traceStart;
    }

    public int getTraceEnd() {
        return traceEnd;
    }
}
