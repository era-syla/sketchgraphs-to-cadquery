import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-2.42749, 1.53215).lineTo(-2.22749, 1.53215).lineTo(-2.22749, 1.72015).lineTo(-2.42749, 1.72015).lineTo(-2.42749, 1.53215).close()
solid=wp_sketch0.add(loop0).extrude(-0.35256687769597195)
