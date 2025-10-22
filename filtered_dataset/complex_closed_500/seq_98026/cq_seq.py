import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.00998, -0.00467).lineTo(-0.00998, -0.00467).lineTo(-0.00998, -0.00061).lineTo(0.00998, -0.00061).lineTo(0.00998, -0.00467).close()
solid=wp_sketch0.add(loop0).extrude(-0.0033110241546126023)
