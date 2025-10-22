import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.0, 0.125).lineTo(-0.011, 0.125).lineTo(-0.011, 0.115).lineTo(-0.013, 0.115).lineTo(-0.013, 0.015).lineTo(-0.007, 0.015).lineTo(-0.007, 0.0).lineTo(0.0, 0.0).lineTo(0.0, 0.125).close()
solid=wp_sketch0.add(loop0).extrude(0.0607299352785764)
