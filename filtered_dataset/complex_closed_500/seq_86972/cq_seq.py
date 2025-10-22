import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.24461, -0.02309).lineTo(0.25961, -0.02309).lineTo(0.25961, -0.03109).lineTo(0.24461, -0.03109).lineTo(0.24461, -0.02309).close()
solid=wp_sketch0.add(loop0).extrude(0.037648237851433536)
