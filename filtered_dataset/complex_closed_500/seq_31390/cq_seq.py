import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.24924, -0.127).lineTo(-0.24924, -0.127).lineTo(-0.24924, 0.127).lineTo(0.24924, 0.127).lineTo(0.24924, -0.127).close()
solid=wp_sketch0.add(loop0).extrude(-0.7261321213706875)
