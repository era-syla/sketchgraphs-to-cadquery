import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.0041, 0.0).lineTo(0.0011, 0.0).lineTo(0.0041, 0.00365).lineTo(0.0041, 0.0).close()
solid=wp_sketch0.add(loop0).extrude(0.00012412922024094243)
