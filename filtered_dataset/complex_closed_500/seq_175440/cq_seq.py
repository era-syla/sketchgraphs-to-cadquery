import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.01068, 0.01901).lineTo(-0.01068, 0.01241).lineTo(-0.00052, 0.01241).lineTo(-0.00052, -0.00791).lineTo(-0.01068, -0.00791).lineTo(-0.01068, -0.02163).lineTo(0.009, -0.02163).lineTo(0.02006, 0.01241).lineTo(0.01017, 0.01862).lineTo(-0.01068, 0.01901).close()
solid=wp_sketch0.add(loop0).extrude(-0.07690436350061441)
