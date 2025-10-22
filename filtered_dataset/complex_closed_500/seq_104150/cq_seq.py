import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.27193, 0.04665).lineTo(-0.17193, 0.04665).lineTo(-0.17193, 0.02165).lineTo(-0.27193, 0.02165).lineTo(-0.27193, 0.04665).close()
solid=wp_sketch0.add(loop0).extrude(-0.2606920382523594)
