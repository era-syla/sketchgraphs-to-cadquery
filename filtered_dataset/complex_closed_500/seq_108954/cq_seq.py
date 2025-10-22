import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.10621, 0.05902).lineTo(0.25121, 0.05902).lineTo(0.25121, 0.04102).lineTo(0.10621, 0.04102).lineTo(0.10621, 0.05902).close()
solid=wp_sketch0.add(loop0).extrude(-0.27212035321280076)
