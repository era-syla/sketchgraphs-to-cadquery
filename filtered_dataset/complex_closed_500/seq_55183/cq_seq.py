import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.9, 2.75).lineTo(0.9, 2.75).lineTo(0.9, -2.75).lineTo(-0.9, -2.75).lineTo(-0.9, 2.75).close()
solid=wp_sketch0.add(loop0).extrude(12.440086526658815)
