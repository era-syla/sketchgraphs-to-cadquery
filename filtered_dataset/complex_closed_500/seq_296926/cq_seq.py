import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.07052, 0.01608).lineTo(-0.03304, 0.02302).lineTo(-0.03304, 0.02043).lineTo(-0.07052, 0.01287).lineTo(-0.07052, 0.01608).close()
solid=wp_sketch0.add(loop0).extrude(0.052418568641699095)
