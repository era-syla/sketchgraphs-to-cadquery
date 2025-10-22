import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.1595, -0.0075).lineTo(0.1595, 0.0).lineTo(0.18165, 0.0).lineTo(0.18165, -0.0075).lineTo(0.17865, -0.0075).lineTo(0.17865, -0.004).lineTo(0.1625, -0.004).lineTo(0.1625, -0.0075).lineTo(0.1595, -0.0075).close()
solid=wp_sketch0.add(loop0).extrude(0.06012560922732216)
