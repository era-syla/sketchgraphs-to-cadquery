import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.0, 0.03).lineTo(0.0, 0.0).lineTo(0.03, 0.0).lineTo(0.03, 0.03).lineTo(0.0, 0.03).close()
solid=wp_sketch0.add(loop0).extrude(0.06783477287343903)
