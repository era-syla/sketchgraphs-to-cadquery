import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.00042, -0.12065).lineTo(-0.00042, -0.12065).lineTo(-0.00042, -0.11985).lineTo(0.00042, -0.11985).lineTo(0.00042, -0.12065).close()
solid=wp_sketch0.add(loop0).extrude(0.0018070498733979562)
