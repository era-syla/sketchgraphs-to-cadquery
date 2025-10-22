import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.0215, 0.208).lineTo(0.3935, 0.208).lineTo(0.3935, 0.10491).lineTo(-0.0215, 0.10491).lineTo(-0.0215, 0.208).close()
solid=wp_sketch0.add(loop0).extrude(0.9989049541447613)
