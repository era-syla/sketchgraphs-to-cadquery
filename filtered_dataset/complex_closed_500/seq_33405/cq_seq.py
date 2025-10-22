import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.065, 0.04213).lineTo(-0.005, 0.04213).lineTo(-0.005, 0.01672).lineTo(-0.065, 0.01672).lineTo(-0.065, 0.04213).close()
solid=wp_sketch0.add(loop0).extrude(0.015128841478518852)
