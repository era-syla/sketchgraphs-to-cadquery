import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.01117, 0.03818).lineTo(0.08289, 0.03818).lineTo(0.08289, 0.00675).lineTo(0.01117, 0.00675).lineTo(0.01117, 0.03818).close()
solid=wp_sketch0.add(loop0).extrude(0.1860604078058143)
