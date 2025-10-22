import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.01479, 0.01125).lineTo(0.02291, 0.01125).lineTo(0.02291, 0.02552).lineTo(0.01479, 0.02552).lineTo(0.01479, 0.01125).close()
solid=wp_sketch0.add(loop0).extrude(-0.0008772459437703777)
