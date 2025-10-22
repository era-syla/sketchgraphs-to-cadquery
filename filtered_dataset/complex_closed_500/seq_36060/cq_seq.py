import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.0, 0.0).lineTo(0.00432, 0.0).lineTo(0.00432, 0.00432).lineTo(0.0, 0.00432).lineTo(0.0, 0.0).close()
solid=wp_sketch0.add(loop0).extrude(0.004869031256366296)
