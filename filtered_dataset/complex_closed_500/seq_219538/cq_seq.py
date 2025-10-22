import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.0585, 0.43048).lineTo(0.0685, 0.43048).lineTo(0.0685, 0.30348).lineTo(-0.0585, 0.30348).lineTo(-0.0585, 0.43048).close()
solid=wp_sketch0.add(loop0).extrude(0.03278375919557743)
