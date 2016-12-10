/**
 * @author Uros Krcadinac
 * 18-Sep-10
 * @version 0.1
 */
package test;

import java.io.IOException;
import java.util.ArrayList;

import com.sun.xml.internal.bind.v2.schemagen.xmlschema.List;

import synesketch.emotion.Emotion;
import synesketch.emotion.EmotionalState;
import synesketch.emotion.Empathyscope;

public class TestSentence {
	
	public static void main(String[] args) throws IOException {
		String line = "I don't love you";
		EmotionalState sentenceState = Empathyscope.getInstance().feel(line);
		ArrayList<Emotion> emotions = (ArrayList<Emotion>) sentenceState.getFirstStrongestEmotions(6);
		
		System.out.println("strongest");
		
		for (Emotion e : emotions){
			System.out.println( e );
		}
		
		System.out.println("all");
		System.out.println(sentenceState.getAngerWeight());
		System.out.println(sentenceState.getDisgustWeight());
		System.out.println(sentenceState.getFearWeight());
		System.out.println(sentenceState.getHappinessWeight());
		System.out.println(sentenceState.getSadnessWeight());
		System.out.println(sentenceState.getSurpriseWeight());
	}

}
