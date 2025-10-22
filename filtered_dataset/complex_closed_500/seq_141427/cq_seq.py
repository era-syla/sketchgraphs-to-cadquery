import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.42207, -0.44003).lineTo(4.93745, 4.07534).lineTo(3.4001, 5.6127).lineTo(4.50636, 6.71896).lineTo(9.91247, 1.31285).lineTo(4.29083, -4.30879).lineTo(0.42207, -0.44003).close()
solid=wp_sketch0.add(loop0).extrude(8.470312976383777)
