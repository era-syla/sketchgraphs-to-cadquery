import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.09843, 0.0762).lineTo(0.09843, 0.0762).lineTo(0.09843, -0.0762).lineTo(-0.09843, -0.0762).lineTo(-0.09843, 0.0762).close()
solid=wp_sketch0.add(loop0).extrude(0.5750197195814248)
