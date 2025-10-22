import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.0, -0.02187).lineTo(-0.0, 0.02187).lineTo(0.15, 0.28168).lineTo(0.15, 0.23794).lineTo(-0.0, -0.02187).close()
solid=wp_sketch0.add(loop0).extrude(-0.5937821174038662)
