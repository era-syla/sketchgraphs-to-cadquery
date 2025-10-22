import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.03994, 0.012).lineTo(0.05194, 0.012).lineTo(0.05194, 0.0).lineTo(0.03994, 0.0).lineTo(0.03994, 0.012).close()
solid=wp_sketch0.add(loop0).extrude(0.01896891008354832)
