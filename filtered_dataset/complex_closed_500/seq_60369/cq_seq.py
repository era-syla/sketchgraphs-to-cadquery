import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.039, 0.012).lineTo(0.039, 0.012).lineTo(0.039, 0.0).lineTo(-0.039, 0.0).lineTo(-0.039, 0.012).close()
solid=wp_sketch0.add(loop0).extrude(0.070098214160735)
