#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Echo Neural Usrp Spy
# Generated: Thu May  2 18:45:46 2019
##################################################

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

from PyQt4 import Qt
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import qtgui
from gnuradio import uhd
from gnuradio import zeromq
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser
import pmt
import sip
import sys
import echo
import time


class echo_neural_usrp_spy(gr.top_block, Qt.QWidget):

    def __init__(self, beta_rrc=0.13, bits_per_symb=2, cfar_thresh=8, cfo_samps=512, corr_reps=2, log_interval=10, packet_len=512, samps_per_symb=2, seed_rx=123678, seed_tx=123432, spy_length=64, spy_thresh=0.1):
        gr.top_block.__init__(self, "Echo Neural Usrp Spy")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Echo Neural Usrp Spy")
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "echo_neural_usrp_spy")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())

        ##################################################
        # Parameters
        ##################################################
        self.beta_rrc = beta_rrc
        self.bits_per_symb = bits_per_symb
        self.cfar_thresh = cfar_thresh
        self.cfo_samps = cfo_samps
        self.corr_reps = corr_reps
        self.log_interval = log_interval
        self.packet_len = packet_len
        self.samps_per_symb = samps_per_symb
        self.seed_rx = seed_rx
        self.seed_tx = seed_tx
        self.spy_length = spy_length
        self.spy_thresh = spy_thresh

        ##################################################
        # Variables
        ##################################################
        self.tx_gain = tx_gain = 4
        self.samp_rate = samp_rate = 500000
        self.rx_gain = rx_gain = 3
        self.cfo_freqs = cfo_freqs = 11./256, 43./256, 97./256
        self.body = body = [1,1,1,1,1,1,1,0,0,1,1,0,0,0,0,1,0,1,1,1,0,1,1,1,1,0,0,1,0,0,1,0,1,0,1,0,1,1,0,1,1,0,0,1,0,0,1,0,0,0,0,0,1,0,0,1,0,0,0,1,1,0,0,0,1,0,0,0,0,1,1,1,1,0,1,1,0,1,0,1,1,0,1,1,1,1,0,1,0,0,0,0,0,0,0,0,0,1,0,1,1,1,1,0,1,0,0,1,1,1,1,1,1,0,1,1,1,0,0,0,1,1,1,1,1,0,1,0,0,0,0,0,1,0,1,0,0,1,0,1,0,1,1,1,1,0,0,1,0,1,1,0,0,1,1,1,0,1,0,0,0,1,0,1,0,1,0,0,1,1,0,1,1,0,1,0,0,0,0,0,0,1,1,0,0,0,0,1,0,0,0,1,0,1,0,0,0,1,0,1,1,0,0,0,1,0,1,0,0,1,1,1,0,0,0,0,1,0,1,1,0,1,1,1,0,0,0,1,1,1,1,1,0,1,1,1,0,0,1,0,1,1,0,1,0,1,0,0,0,0,1,1,1,0,1,0,0,0,1,1,1,0,1,0,0,0,0,1,1,0,0,1,1,0,0,1,1,1,0,0,0,1,1,0,0,1,1,0,1,0,1,0,1,0,1,0,0,0,1,1,0,1,1,1,0,0,1,1,1,1,1,0,0,1,0,0,1,0,1,0,1,0,0,1,0,0,1,0,1,0,1,1,1,0,0,1,0,1,1,1,0,1,1,0,1,0,1,1,1,1,1,0,1,1,1,0,1,0,1,0,1,0,0,0,1,0,1,1,0,1,0,1,1,1,1,1,1,0,1,1,0,0,0,1,0,0,1,1,1,1,0,0,1,0,0,0,0,1,0,0,1,0,1,0,0,0,0,1,1,1,1,0,0,0,1,0,0,1,0,1,1,0,1,0,1,0,1,0,1,0,0,0,0,1,1,0,1,0,1,1,0,0,1,0,1,1,1,1,0,1,1,0,0,0,0,1,1,0,0,0,0,1,1,0,1,0,1,0,0,0,0,1,1,0,0,0,1,0,0,1,0,1,0,0,0,1,0,1,1,0,1,1,1,1,1,1,0,0,1,0,0,1,0,0,1,0,0,0,0,1,1,0]
        self.F_center = F_center = 1000000000

        ##################################################
        # Blocks
        ##################################################
        self.zeromq_pull_msg_source_0_0 = zeromq.pull_msg_source("tcp://127.0.0.1:5555", 100, True)
        self.zeromq_pull_msg_source_0 = zeromq.pull_msg_source("tcp://127.0.0.1:5556", 100, True)
        self.uhd_usrp_source_0 = uhd.usrp_source(
        	",".join(("", "")),
        	uhd.stream_args(
        		cpu_format="fc32",
        		channels=range(2),
        	),
        )
        self.uhd_usrp_source_0.set_samp_rate(samp_rate)
        self.uhd_usrp_source_0.set_center_freq(F_center, 0)
        self.uhd_usrp_source_0.set_gain(20, 0)
        self.uhd_usrp_source_0.set_antenna("RX2", 0)
        self.uhd_usrp_source_0.set_center_freq(F_center, 1)
        self.uhd_usrp_source_0.set_gain(rx_gain, 1)
        self.uhd_usrp_source_0.set_antenna("RX2", 1)
        self.uhd_usrp_sink_0 = uhd.usrp_sink(
        	",".join(("", "")),
        	uhd.stream_args(
        		cpu_format="fc32",
        		channels=range(1),
        	),
        	"packet_len",
        )
        self.uhd_usrp_sink_0.set_samp_rate(samp_rate)
        self.uhd_usrp_sink_0.set_center_freq(F_center, 0)
        self.uhd_usrp_sink_0.set_gain(tx_gain, 0)
        self.uhd_usrp_sink_0.set_antenna("TX/RX", 0)
        self.echo_watchdog_0 = echo.watchdog(5)
        self.echo_preamble_insert_0_0 = echo.preamble_insert((body), 1, 0, 0)
        self.echo_packet_length_check_0 = echo.packet_length_check((2 * packet_len + spy_length) / bits_per_symb)
        self.echo_modulator_neural_spy_0 = echo.modulator_neural_spy(seed=seed_tx, hidden_layers=(20, ),
              bits_per_symbol=bits_per_symb, preamble=(body),
              log_constellation_interval=log_interval, init_weights="",
              spy_length=spy_length)
        self.echo_demodulator_neural_spy_0 = echo.demodulator_neural_spy(seed=seed_rx, hidden_layers=(20, ),
              bits_per_symbol=bits_per_symb, preamble=(body),
              log_constellation_interval=log_interval, init_weights="",
              spy_length=spy_length, spy_threshold=spy_thresh)
        self.qtgui_const_sink_x_0_0_0 = qtgui.const_sink_c(
        	(2 * packet_len + spy_length) / bits_per_symb, #size
        	"Channel IQ Scatter", #name
        	1 #number of inputs
        )
        self.qtgui_const_sink_x_0_0_0.set_update_time(0.0)
        self.qtgui_const_sink_x_0_0_0.set_y_axis(-2, 2)
        self.qtgui_const_sink_x_0_0_0.set_x_axis(-2, 2)
        self.qtgui_const_sink_x_0_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, "")
        self.qtgui_const_sink_x_0_0_0.enable_autoscale(True)
        self.qtgui_const_sink_x_0_0_0.enable_grid(True)
        
        if not True:
          self.qtgui_const_sink_x_0_0_0.disable_legend()
        
        labels = ["", "", "", "", "",
                  "", "", "", "", ""]
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "red", "red", "red",
                  "red", "red", "red", "red", "red"]
        styles = [0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0]
        markers = [0, 0, 0, 0, 0,
                   0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_const_sink_x_0_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_const_sink_x_0_0_0.set_line_label(i, labels[i])
            self.qtgui_const_sink_x_0_0_0.set_line_width(i, widths[i])
            self.qtgui_const_sink_x_0_0_0.set_line_color(i, colors[i])
            self.qtgui_const_sink_x_0_0_0.set_line_style(i, styles[i])
            self.qtgui_const_sink_x_0_0_0.set_line_marker(i, markers[i])
            self.qtgui_const_sink_x_0_0_0.set_line_alpha(i, alphas[i])
        
        self._qtgui_const_sink_x_0_0_0_win = sip.wrapinstance(self.qtgui_const_sink_x_0_0_0.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_const_sink_x_0_0_0_win)
        self.qtgui_const_sink_x_0_0 = qtgui.const_sink_c(
        	(2 * packet_len + spy_length) / bits_per_symb, #size
        	"Detected Body Constellation", #name
        	1 #number of inputs
        )
        self.qtgui_const_sink_x_0_0.set_update_time(0.0)
        self.qtgui_const_sink_x_0_0.set_y_axis(-2, 2)
        self.qtgui_const_sink_x_0_0.set_x_axis(-2, 2)
        self.qtgui_const_sink_x_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, "")
        self.qtgui_const_sink_x_0_0.enable_autoscale(False)
        self.qtgui_const_sink_x_0_0.enable_grid(True)
        
        if not True:
          self.qtgui_const_sink_x_0_0.disable_legend()
        
        labels = ["", "", "", "", "",
                  "", "", "", "", ""]
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "red", "red", "red",
                  "red", "red", "red", "red", "red"]
        styles = [0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0]
        markers = [0, 0, 0, 0, 0,
                   0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_const_sink_x_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_const_sink_x_0_0.set_line_label(i, labels[i])
            self.qtgui_const_sink_x_0_0.set_line_width(i, widths[i])
            self.qtgui_const_sink_x_0_0.set_line_color(i, colors[i])
            self.qtgui_const_sink_x_0_0.set_line_style(i, styles[i])
            self.qtgui_const_sink_x_0_0.set_line_marker(i, markers[i])
            self.qtgui_const_sink_x_0_0.set_line_alpha(i, alphas[i])
        
        self._qtgui_const_sink_x_0_0_win = sip.wrapinstance(self.qtgui_const_sink_x_0_0.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_const_sink_x_0_0_win)
        self.neural_to_classic_handler = echo.packet_handler(cfo_samps, corr_reps, (2 * packet_len + spy_length) / bits_per_symb, cfar_thresh, samps_per_symb, beta_rrc, (cfo_freqs))
        self.blocks_random_pdu_0 = blocks.random_pdu(packet_len, packet_len, chr(0x01), 1)
        self.blocks_pdu_to_tagged_stream_0_1_0 = blocks.pdu_to_tagged_stream(blocks.complex_t, "pkt")
        self.blocks_pdu_to_tagged_stream_0_1 = blocks.pdu_to_tagged_stream(blocks.complex_t, "pkt")
        self.blocks_null_sink_0 = blocks.null_sink(gr.sizeof_gr_complex*1)

        ##################################################
        # Connections
        ##################################################
        self.msg_connect((self.blocks_random_pdu_0, 'pdus'), (self.echo_preamble_insert_0_0, 'in'))    
        self.msg_connect((self.neural_to_classic_handler, 'unwrap_out'), (self.blocks_pdu_to_tagged_stream_0_1, 'pdus'))    
        self.msg_connect((self.neural_to_classic_handler, 'unwrap_out'), (self.echo_packet_length_check_0, 'in'))    
        self.msg_connect((self.echo_demodulator_neural_spy_0, 'corrupt'), (self.blocks_random_pdu_0, 'generate'))    
        self.msg_connect((self.echo_demodulator_neural_spy_0, 'bits'), (self.echo_modulator_neural_spy_0, 'feedback'))    
        self.msg_connect((self.echo_modulator_neural_spy_0, 'symbols'), (self.blocks_pdu_to_tagged_stream_0_1_0, 'pdus'))    
        self.msg_connect((self.echo_modulator_neural_spy_0, 'symbols'), (self.neural_to_classic_handler, 'wrap_in'))    
        self.msg_connect((self.echo_packet_length_check_0, 'failed'), (self.blocks_random_pdu_0, 'generate'))    
        self.msg_connect((self.echo_packet_length_check_0, 'validated'), (self.echo_demodulator_neural_spy_0, 'symbols'))    
        self.msg_connect((self.echo_packet_length_check_0, 'passthrough'), (self.echo_watchdog_0, 'in'))    
        self.msg_connect((self.echo_preamble_insert_0_0, 'out'), (self.echo_modulator_neural_spy_0, 'bits'))    
        self.msg_connect((self.echo_watchdog_0, 'out'), (self.blocks_random_pdu_0, 'generate'))    
        self.msg_connect((self.zeromq_pull_msg_source_0, 'out'), (self.echo_demodulator_neural_spy_0, 'control'))    
        self.msg_connect((self.zeromq_pull_msg_source_0, 'out'), (self.uhd_usrp_source_0, 'command'))    
        self.msg_connect((self.zeromq_pull_msg_source_0_0, 'out'), (self.echo_modulator_neural_spy_0, 'control'))    
        self.msg_connect((self.zeromq_pull_msg_source_0_0, 'out'), (self.uhd_usrp_sink_0, 'command'))    
        self.connect((self.blocks_pdu_to_tagged_stream_0_1, 0), (self.qtgui_const_sink_x_0_0, 0))    
        self.connect((self.blocks_pdu_to_tagged_stream_0_1_0, 0), (self.qtgui_const_sink_x_0_0_0, 0))    
        self.connect((self.neural_to_classic_handler, 0), (self.uhd_usrp_sink_0, 0))    
        self.connect((self.uhd_usrp_source_0, 0), (self.blocks_null_sink_0, 0))    
        self.connect((self.uhd_usrp_source_0, 1), (self.neural_to_classic_handler, 0))    

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "echo_neural_usrp_spy")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()


    def get_beta_rrc(self):
        return self.beta_rrc

    def set_beta_rrc(self, beta_rrc):
        self.beta_rrc = beta_rrc

    def get_bits_per_symb(self):
        return self.bits_per_symb

    def set_bits_per_symb(self, bits_per_symb):
        self.bits_per_symb = bits_per_symb

    def get_cfar_thresh(self):
        return self.cfar_thresh

    def set_cfar_thresh(self, cfar_thresh):
        self.cfar_thresh = cfar_thresh

    def get_cfo_samps(self):
        return self.cfo_samps

    def set_cfo_samps(self, cfo_samps):
        self.cfo_samps = cfo_samps

    def get_corr_reps(self):
        return self.corr_reps

    def set_corr_reps(self, corr_reps):
        self.corr_reps = corr_reps

    def get_log_interval(self):
        return self.log_interval

    def set_log_interval(self, log_interval):
        self.log_interval = log_interval

    def get_packet_len(self):
        return self.packet_len

    def set_packet_len(self, packet_len):
        self.packet_len = packet_len

    def get_samps_per_symb(self):
        return self.samps_per_symb

    def set_samps_per_symb(self, samps_per_symb):
        self.samps_per_symb = samps_per_symb

    def get_seed_rx(self):
        return self.seed_rx

    def set_seed_rx(self, seed_rx):
        self.seed_rx = seed_rx

    def get_seed_tx(self):
        return self.seed_tx

    def set_seed_tx(self, seed_tx):
        self.seed_tx = seed_tx

    def get_spy_length(self):
        return self.spy_length

    def set_spy_length(self, spy_length):
        self.spy_length = spy_length

    def get_spy_thresh(self):
        return self.spy_thresh

    def set_spy_thresh(self, spy_thresh):
        self.spy_thresh = spy_thresh

    def get_tx_gain(self):
        return self.tx_gain

    def set_tx_gain(self, tx_gain):
        self.tx_gain = tx_gain
        self.uhd_usrp_sink_0.set_gain(self.tx_gain, 0)
        	

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.uhd_usrp_sink_0.set_samp_rate(self.samp_rate)
        self.uhd_usrp_source_0.set_samp_rate(self.samp_rate)

    def get_rx_gain(self):
        return self.rx_gain

    def set_rx_gain(self, rx_gain):
        self.rx_gain = rx_gain
        self.uhd_usrp_source_0.set_gain(self.rx_gain, 1)
        	

    def get_cfo_freqs(self):
        return self.cfo_freqs

    def set_cfo_freqs(self, cfo_freqs):
        self.cfo_freqs = cfo_freqs

    def get_body(self):
        return self.body

    def set_body(self, body):
        self.body = body

    def get_F_center(self):
        return self.F_center

    def set_F_center(self, F_center):
        self.F_center = F_center
        self.uhd_usrp_sink_0.set_center_freq(self.F_center, 0)
        self.uhd_usrp_source_0.set_center_freq(self.F_center, 0)
        self.uhd_usrp_source_0.set_center_freq(self.F_center, 1)


def argument_parser():
    parser = OptionParser(option_class=eng_option, usage="%prog: [options]")
    parser.add_option(
        "", "--beta-rrc", dest="beta_rrc", type="eng_float", default=eng_notation.num_to_str(0.13),
        help="Set RRC Beta [default=%default]")
    parser.add_option(
        "", "--bits-per-symb", dest="bits_per_symb", type="intx", default=2,
        help="Set Bits Per Symbol [default=%default]")
    parser.add_option(
        "", "--cfar-thresh", dest="cfar_thresh", type="eng_float", default=eng_notation.num_to_str(8),
        help="Set CFAR Threshold [default=%default]")
    parser.add_option(
        "", "--cfo-samps", dest="cfo_samps", type="intx", default=512,
        help="Set CFO Samples [default=%default]")
    parser.add_option(
        "", "--corr-reps", dest="corr_reps", type="intx", default=2,
        help="Set Correlator Repetitions [default=%default]")
    parser.add_option(
        "", "--log-interval", dest="log_interval", type="intx", default=10,
        help="Set Constellation Log Interval [default=%default]")
    parser.add_option(
        "", "--packet-len", dest="packet_len", type="intx", default=512,
        help="Set Packet Length [default=%default]")
    parser.add_option(
        "", "--samps-per-symb", dest="samps_per_symb", type="intx", default=2,
        help="Set Samples Per Symbol [default=%default]")
    parser.add_option(
        "", "--seed-rx", dest="seed_rx", type="intx", default=123678,
        help="Set seed_rx [default=%default]")
    parser.add_option(
        "", "--seed-tx", dest="seed_tx", type="intx", default=123432,
        help="Set seed_tx [default=%default]")
    parser.add_option(
        "", "--spy-length", dest="spy_length", type="intx", default=64,
        help="Set Spy Length [default=%default]")
    parser.add_option(
        "", "--spy-thresh", dest="spy_thresh", type="eng_float", default=eng_notation.num_to_str(0.1),
        help="Set Spy Threshold [default=%default]")
    return parser


def main(top_block_cls=echo_neural_usrp_spy, options=None):
    if options is None:
        options, _ = argument_parser().parse_args()

    from distutils.version import StrictVersion
    if StrictVersion(Qt.qVersion()) >= StrictVersion("4.5.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls(beta_rrc=options.beta_rrc, bits_per_symb=options.bits_per_symb, cfar_thresh=options.cfar_thresh, cfo_samps=options.cfo_samps, corr_reps=options.corr_reps, log_interval=options.log_interval, packet_len=options.packet_len, samps_per_symb=options.samps_per_symb, seed_rx=options.seed_rx, seed_tx=options.seed_tx, spy_length=options.spy_length, spy_thresh=options.spy_thresh)
    tb.start()
    tb.show()

    def quitting():
        tb.stop()
        tb.wait()
    qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), quitting)
    qapp.exec_()


if __name__ == '__main__':
    main()
