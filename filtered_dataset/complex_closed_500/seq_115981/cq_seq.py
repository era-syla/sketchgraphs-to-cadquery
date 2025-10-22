import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.01588, -0.00114).lineTo(-0.01588, 0.0).lineTo(-0.01686, -0.00057).lineTo(-0.01588, -0.00114).close()
solid=wp_sketch0.add(loop0).extrude(-0.0007498811385683363)
