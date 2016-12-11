package synesketch.emotion.util;

import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;
import java.util.StringTokenizer;

import synesketch.emotion.AffectWord;
import synesketch.util.PropertiesManager;

/**
 * Utility class for some text preprocessing
 * 
 * @author Ryorda Triaptahadi
 * @email triaptahadiryorda@yahoo.co.id
 * @version 1.0
 */
public class PreprocessingUtility {

	private static PreprocessingUtility instance;
	
	private String fileNameContraction = "/data/lex/lexicon_contractions.csv";
	
	private PreprocessingUtility()  {
		
	}

	/**
	 * Returns the Singleton instance of the {@link LexicalUtility}.
	 * 
	 * @return the instance of {@link LexicalUtility}
	 * @throws IOException
	 */
	public static PreprocessingUtility getInstance()  {
		if (instance == null) {
			instance = new PreprocessingUtility();
		}
		return instance;
	}
	
	public String preprocessContractions(String sentence) {
		try {
			
			BufferedReader in = new BufferedReader(new InputStreamReader(this
					.getClass().getResourceAsStream(fileNameContraction), "UTF8"));
			
			String line;
			String newSentence = sentence.toString();
			
			while (( line = in.readLine() ) != null){
				String[] words = line.split(",");
				String regex = words[0].replaceAll("[’']", "[’']");
				newSentence = newSentence.replaceAll( "(?i)" + regex, words[1]);
			}
			
			return newSentence;
		} catch (FileNotFoundException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
			return sentence;
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
			return sentence;
		}
	}
}
