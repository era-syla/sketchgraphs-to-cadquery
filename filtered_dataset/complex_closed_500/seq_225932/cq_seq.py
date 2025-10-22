import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.03687, 0.01581).lineTo(0.03687, 0.02057).lineTo(0.03857, 0.01645).lineTo(0.03857, 0.01581).lineTo(0.03687, 0.01581).close()
solid=wp_sketch0.add(loop0).extrude(-0.01049238979489196)
