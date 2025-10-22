import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(2.71651, 0.50453).lineTo(3.04575, 0.50453).lineTo(3.04575, -0.3114).lineTo(2.71651, -0.3114).lineTo(2.71651, 0.50453).close()
solid=wp_sketch0.add(loop0).extrude(-0.10910029744069454)
