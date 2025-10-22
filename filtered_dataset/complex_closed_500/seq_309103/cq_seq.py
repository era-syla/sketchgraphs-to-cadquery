import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.02275, 0.019).lineTo(-0.02725, 0.0235).lineTo(-0.02725, 0.019).lineTo(-0.02275, 0.019).close()
solid=wp_sketch0.add(loop0).extrude(0.011887606070602259)
