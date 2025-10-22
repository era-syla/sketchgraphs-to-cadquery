import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-3.7849, 4.11293).lineTo(-1.7149, 4.11293).lineTo(-1.7149, 4.07293).lineTo(-3.7849, 4.07293).lineTo(-3.7849, 4.11293).close()
solid=wp_sketch0.add(loop0).extrude(2.6127347604094506)
