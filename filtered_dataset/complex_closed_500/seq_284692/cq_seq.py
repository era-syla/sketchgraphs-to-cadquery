import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.12748, -0.06504).lineTo(-0.15748, -0.06504).lineTo(-0.15748, -0.10504).lineTo(-0.12748, -0.10504).lineTo(-0.12748, -0.06504).close()
solid=wp_sketch0.add(loop0).extrude(-0.10924413032267896)
