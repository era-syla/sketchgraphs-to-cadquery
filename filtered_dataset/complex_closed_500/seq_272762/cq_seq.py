import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.18102, -0.03501).lineTo(0.17889, -0.03501).lineTo(0.17889, -0.03651).lineTo(0.18102, -0.03651).lineTo(0.18102, -0.03501).close()
solid=wp_sketch0.add(loop0).extrude(-0.0004960430162737539)
