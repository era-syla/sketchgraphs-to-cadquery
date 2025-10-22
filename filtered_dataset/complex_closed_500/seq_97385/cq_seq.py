import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.031, 0.0).lineTo(0.0, 0.0).lineTo(0.0, 0.016).lineTo(0.031, 0.016).lineTo(0.031, 0.086).lineTo(-0.031, 0.086).lineTo(-0.031, 0.0).close()
solid=wp_sketch0.add(loop0).extrude(-0.0991876586123654)
