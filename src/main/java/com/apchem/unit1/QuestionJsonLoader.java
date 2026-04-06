package com.apchem.unit1;

import com.google.gson.Gson;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.nio.charset.StandardCharsets;
import java.util.ArrayList;
import java.util.List;

/**
 * Loads {@code McqQuestion} items from {@code /questions.json} on the classpath (mirrors the website
 * {@code questions.json} in the repo root).
 */
public final class QuestionJsonLoader {
  private QuestionJsonLoader() {}

  public static List<McqQuestion> load() {
    InputStream in = QuestionJsonLoader.class.getClassLoader().getResourceAsStream("questions.json");
    if (in == null) {
      throw new IllegalStateException("Missing resource questions.json (copy from repo root after expansion)");
    }
    Gson gson = new Gson();
    RawQuestion[] raw;
    try (InputStreamReader reader = new InputStreamReader(in, StandardCharsets.UTF_8)) {
      raw = gson.fromJson(reader, RawQuestion[].class);
    } catch (Exception e) {
      throw new IllegalStateException("Failed to parse questions.json", e);
    }
    List<McqQuestion> out = new ArrayList<>();
    for (RawQuestion rq : raw) {
      List<McqOption> options = new ArrayList<>();
      for (RawOption ro : rq.options) {
        options.add(new McqOption(ro.label, ro.text, ro.rationale));
      }
      Subsection sub = Subsection.fromCedLabel(rq.subsection);
      out.add(new McqQuestion(sub, rq.stimulus, rq.stem, options, rq.correct));
    }
    return List.copyOf(out);
  }

  /** Gson-friendly DTO matching {@code questions.json} objects. */
  public static final class RawQuestion {
    public String subsection;
    public String stimulus;
    public String stem;
    public String correct;
    public RawOption[] options;
  }

  public static final class RawOption {
    public String label;
    public String text;
    public String rationale;
  }
}
