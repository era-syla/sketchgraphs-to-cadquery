import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.54573, -1.29872).lineTo(0.67427, -1.29872).lineTo(0.67427, 1.14128).lineTo(-0.54573, 1.14128).lineTo(-0.54573, -1.29872).close()
solid=wp_sketch0.add(loop0).extrude(-1.504815262764091)
