import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.00075, 0.011).lineTo(-0.0025, 0.007).lineTo(-0.00259, 0.007).lineTo(-0.00259, 0.011).lineTo(-0.00075, 0.011).close()
solid=wp_sketch0.add(loop0).extrude(-0.006047417638001028)
