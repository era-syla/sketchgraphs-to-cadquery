import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.85725, 0.00635).lineTo(1.108, 0.26759).lineTo(0.85725, 0.26759).lineTo(0.85725, 0.00635).close()
solid=wp_sketch0.add(loop0).extrude(-0.28320763784579295)
