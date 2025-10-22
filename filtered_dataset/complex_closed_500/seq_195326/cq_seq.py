import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.0172, -0.01511).lineTo(-0.06784, -0.01491).lineTo(-0.07039, -0.04437).lineTo(0.0172, -0.04437).lineTo(0.0172, -0.01511).close()
solid=wp_sketch0.add(loop0).extrude(-0.12223195233217794)
