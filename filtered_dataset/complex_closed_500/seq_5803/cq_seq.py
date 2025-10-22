import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.05, 0.0444).lineTo(0.05, 0.0444).lineTo(0.05, -0.0444).lineTo(-0.05, -0.0444).lineTo(-0.05, 0.0444).close()
solid=wp_sketch0.add(loop0).extrude(-0.10309206533796356)
