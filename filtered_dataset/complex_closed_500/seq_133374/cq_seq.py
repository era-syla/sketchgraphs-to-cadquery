import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.0, 3.0).lineTo(-3.0, 5.06533).lineTo(-6.0, 3.0).lineTo(0.0, 3.0).close()
solid=wp_sketch0.add(loop0).extrude(0.3441771926493047)
