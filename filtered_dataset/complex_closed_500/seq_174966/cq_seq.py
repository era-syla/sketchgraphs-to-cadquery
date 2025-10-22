import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.03147, 0.0365).lineTo(0.03944, 0.0365).lineTo(0.03944, -0.02569).lineTo(-0.03147, -0.02569).lineTo(-0.03147, 0.0365).close()
solid=wp_sketch0.add(loop0).extrude(-0.2008673159631737)
