import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.0, 0.0).lineTo(0.0, 0.04).lineTo(-0.01725, 0.04).lineTo(-0.01725, 0.025).lineTo(-0.02, 0.02).lineTo(-0.02, 0.0).lineTo(0.0, 0.0).close()
solid=wp_sketch0.add(loop0).extrude(0.08852418353420749)
