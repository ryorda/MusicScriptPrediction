package synesketch.emotion.util;

import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.HashMap;
import java.util.Map;
import java.util.StringTokenizer;

import sun.util.locale.StringTokenIterator;

/**
 * Utility class for some text preprocessing
 * 
 * @author Ryorda Triaptahadi
 * @email triaptahadiryorda@yahoo.co.id
 * @version 1.0
 */
public class PreprocessingUtility {

	private static String fileNameContraction = "data/lex/lexicon_contractions.csv";
	
	public static String preprocessContractions(String sentence) {
		try {
			Map<String, String> contractions = new HashMap<String,String>();
			
			BufferedReader bf = new BufferedReader( new FileReader( fileNameContraction ) );
			String line;
			
			while (( line = bf.readLine() ) != null){
				String[] words = line.split(",");
				contractions.put(words[0], words[1]);
			}
			
			StringBuilder sb = new StringBuilder();
			
			StringTokenizer ss = new StringTokenizer(sentence, " ");
			
			while (ss.hasMoreTokens()){
				String token = ss.nextToken();
				String cont = contractions.get(token);
				sb.append( cont == null ? token : cont);
			}
			
			return sb.toString();
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
