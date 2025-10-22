import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-1.32, 0.0).lineTo(0.0, 0.0).lineTo(0.0, 1.28).lineTo(-1.32, 1.28).lineTo(-1.32, 0.0).close()
solid=wp_sketch0.add(loop0).extrude(-0.8759267099062125)
