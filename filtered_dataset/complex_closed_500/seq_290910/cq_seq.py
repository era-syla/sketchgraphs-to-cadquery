import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.0, -0.15).lineTo(1.5, -0.15).lineTo(1.5, -0.88).lineTo(1.8, -0.88).lineTo(1.8, -1.13).lineTo(2.02, -1.13).lineTo(2.02, -0.88).lineTo(2.72, -0.88).lineTo(2.72, -3.9).lineTo(2.02, -3.9).lineTo(2.02, -3.65).lineTo(1.8, -3.65).lineTo(1.8, -3.9).lineTo(1.5, -3.9).lineTo(1.5, -4.4).lineTo(0.0, -4.4).lineTo(0.0, -0.15).close()
solid=wp_sketch0.add(loop0).extrude(11.768521012077148)
