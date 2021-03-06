/* -*- c++ -*- */
/* 
 * Copyright 2018 <+YOU OR YOUR COMPANY+>.
 * 
 * This is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; either version 3, or (at your option)
 * any later version.
 * 
 * This software is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 * 
 * You should have received a copy of the GNU General Public License
 * along with this software; see the file COPYING.  If not, write to
 * the Free Software Foundation, Inc., 51 Franklin Street,
 * Boston, MA 02110-1301, USA.
 */

#ifndef INCLUDED_ECHO_PDU_COMPLEX_TO_ETTUS_TAGGED_STREAM_IMPL_H
#define INCLUDED_ECHO_PDU_COMPLEX_TO_ETTUS_TAGGED_STREAM_IMPL_H

#include <echo/pdu_complex_to_ettus_tagged_stream.h>

namespace gr {
  namespace echo {

    class pdu_complex_to_ettus_tagged_stream_impl : public pdu_complex_to_ettus_tagged_stream
    {
     private:
       size_t                       d_itemsize;
       gr::blocks::pdu::vector_type d_type;
       pmt::pmt_t                   d_curr_meta;
       pmt::pmt_t                   d_curr_vect;
       size_t                       d_curr_len;
       std::string                  d_sob_tag_name;
       std::string                  d_eob_tag_name;
       int                          d_timeout_ms;

     protected:
      int calculate_output_stream_length(const gr_vector_int &ninput_items);

     public:
      pdu_complex_to_ettus_tagged_stream_impl(const std::string& length_tag_name, const std::string& sob_tag_name, const std::string& eob_tag_name, int timeout_ms);
      ~pdu_complex_to_ettus_tagged_stream_impl();

      // Where all the action really happens
      int work(int noutput_items,
           gr_vector_int &ninput_items,
           gr_vector_const_void_star &input_items,
           gr_vector_void_star &output_items);
    };

  } // namespace echo
} // namespace gr

#endif /* INCLUDED_ECHO_PDU_COMPLEX_TO_ETTUS_TAGGED_STREAM_IMPL_H */

